# ============================================
# TAO 8 DATABASE + 8 USER POSTGRESQL
# ============================================
. "$PSScriptRoot\00_config.ps1"

$env:PGPASSWORD = $Global:PgSuperPassword

Write-Host "`n=== TAO DATABASE + USER POSTGRESQL ===" -ForegroundColor Cyan

# Build SQL
$sqlLines = @()
foreach ($svc in $Global:Services) {
    $sqlLines += "DROP DATABASE IF EXISTS $($svc.DB);"
}
foreach ($svc in $Global:Services) {
    $sqlLines += "DROP USER IF EXISTS $($svc.User);"
}
foreach ($svc in $Global:Services) {
    $sqlLines += "CREATE USER $($svc.User) WITH PASSWORD '$($svc.Password)';"
}
foreach ($svc in $Global:Services) {
    $sqlLines += "CREATE DATABASE $($svc.DB) OWNER $($svc.User) TEMPLATE template0 ENCODING 'UTF8' LC_COLLATE 'C' LC_CTYPE 'C';"
}
foreach ($svc in $Global:Services) {
    $sqlLines += "GRANT ALL PRIVILEGES ON DATABASE $($svc.DB) TO $($svc.User);"
}

$sqlFile = "$Global:MigDir\create_dbs.sql"
$sqlLines -join "`r`n" | Set-Content -Path $sqlFile -Encoding UTF8
Write-Host "Da tao: $sqlFile" -ForegroundColor Cyan

& $Global:PsqlPath -U $Global:PgSuperUser -h localhost -p 5432 -f $sqlFile

if ($LASTEXITCODE -eq 0) {
    Write-Host "`nOK! 8 database + 8 user da tao." -ForegroundColor Green
} else {
    Write-Host "`nLOI! Xem output ben tren." -ForegroundColor Red
}

# Verify
Write-Host "`n=== DANH SACH DATABASE ===" -ForegroundColor Cyan
& $Global:PsqlPath -U $Global:PgSuperUser -h localhost -p 5432 -c "\l" | Select-String "humg_"

$env:PGPASSWORD = $null