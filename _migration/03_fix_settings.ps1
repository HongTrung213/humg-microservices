# ============================================
# SUA settings.py - DOI SQLITE -> POSTGRESQL
# ============================================
. "$PSScriptRoot\00_config.ps1"

Write-Host "`n=== SUA settings.py ===" -ForegroundColor Cyan

foreach ($svc in $Global:Services) {
    $settingsPath = Join-Path $Global:BaseDir "$($svc.Folder)\$($svc.Package)\settings.py"

    if (-not (Test-Path $settingsPath)) {
        Write-Host "SKIP: $settingsPath" -ForegroundColor Yellow
        continue
    }

    # Backup
    $backup = "$settingsPath.before_postgres"
    if (-not (Test-Path $backup)) {
        Copy-Item $settingsPath $backup -Force
    }

    $content = Get-Content $settingsPath -Raw -Encoding UTF8

    # Kiem tra da doi chua
    if ($content -match "django.db.backends.postgresql") {
        Write-Host "SKIP: $($svc.Folder) da la PostgreSQL" -ForegroundColor DarkGray
        continue
    }

    # Build DATABASES moi
    $newDatabases = @"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', '$($svc.DB)'),
        'USER': os.getenv('DB_USER', '$($svc.User)'),
        'PASSWORD': os.getenv('DB_PASSWORD', '$($svc.Password)'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
        'CONN_MAX_AGE': 600,
        'CONN_HEALTH_CHECKS': True,
        'OPTIONS': {
            'connect_timeout': 10,
        },
    }
}
"@

    $pattern = '(?s)DATABASES\s*=\s*\{.*?\n\}'

    if ($content -match $pattern) {
        $content = $content -replace $pattern, $newDatabases
        Set-Content -Path $settingsPath -Value $content -Encoding UTF8 -NoNewline
        Write-Host "OK $($svc.Folder)" -ForegroundColor Green
    } else {
        Write-Host "WARN: Khong match DATABASES trong $($svc.Folder)" -ForegroundColor Yellow
    }
}

Write-Host "`nDone!" -ForegroundColor Green