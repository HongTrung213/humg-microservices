# ============================================
# MIGRATE POSTGRESQL + TEST
# ============================================
. "$PSScriptRoot\00_config.ps1"

Write-Host "`n=== MIGRATE 8 SERVICE ===" -ForegroundColor Cyan

$okCount = 0
$failCount = 0

foreach ($svc in $Global:Services) {
    $svcPath = Join-Path $Global:BaseDir $svc.Folder

    Write-Host "`n--- $($svc.Folder) -> $($svc.DB) ---" -ForegroundColor Cyan
    Push-Location $svcPath

    # Check Django
    python manage.py check 2>&1 | Out-Null

    # Migrate
    python manage.py migrate --noinput

    if ($LASTEXITCODE -eq 0) {
        Write-Host "OK migrate $($svc.Folder)" -ForegroundColor Green
        $okCount++
    } else {
        Write-Host "LOI migrate $($svc.Folder)" -ForegroundColor Red
        $failCount++
    }

    Pop-Location
}

Write-Host "`n=== KET QUA ===" -ForegroundColor Cyan
Write-Host "OK: $okCount" -ForegroundColor Green
if ($failCount -gt 0) {
    Write-Host "FAILED: $failCount" -ForegroundColor Red
}