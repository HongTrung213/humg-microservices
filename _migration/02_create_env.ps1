# ============================================
# TAO .env CHO 8 SERVICE
# ============================================
. "$PSScriptRoot\00_config.ps1"

Write-Host "`n=== TAO .env CHO 8 SERVICE ===" -ForegroundColor Cyan

foreach ($svc in $Global:Services) {
    $svcPath = Join-Path $Global:BaseDir $svc.Folder
    $envFile = Join-Path $svcPath ".env"

    if (-not (Test-Path $svcPath)) {
        Write-Host "SKIP: $svcPath khong ton tai" -ForegroundColor Yellow
        continue
    }

    # Backup .env cu
    if (Test-Path $envFile) {
        $backup = "$envFile.before_postgres_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
        Copy-Item $envFile $backup -Force
    }

    $envContent = @"
SECRET_KEY=django-insecure-xxxxxxxxxxxxx
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=$($svc.DB)
DB_USER=$($svc.User)
DB_PASSWORD=$($svc.Password)
DB_HOST=localhost
DB_PORT=5432
"@

    Set-Content -Path $envFile -Value $envContent -Encoding UTF8
    Write-Host "OK $($svc.Folder) -> .env" -ForegroundColor Green
}

Write-Host "`nDone!" -ForegroundColor Green