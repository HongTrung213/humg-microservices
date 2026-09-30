# ============================================
# CONFIG CHUNG
# ============================================
$Global:BaseDir   = "D:\CODE\humg-microservices"
$Global:MigDir    = "$Global:BaseDir\_migration"
$Global:BackupDir = "$Global:MigDir\backup"
$Global:DumpDir   = "$Global:MigDir\dumps"

@($Global:MigDir, $Global:BackupDir, $Global:DumpDir) | ForEach-Object {
    New-Item -ItemType Directory -Force -Path $_ | Out-Null
}

$Global:Services = @(
    @{ Folder = "api-gateway";          Package = "gateway";              DB = "humg_gateway";      User = "humg_gateway";      Password = "gateway_pwd_2026"; Port = 8000 },
    @{ Folder = "student-service";      Package = "student_service";      DB = "humg_student";      User = "humg_student";      Password = "student_pwd_2026"; Port = 8001 },
    @{ Folder = "training-service";     Package = "training_service";     DB = "humg_training";     User = "humg_training";     Password = "training_pwd_2026"; Port = 8002 },
    @{ Folder = "exam-service";         Package = "exam_service";         DB = "humg_exam";         User = "humg_exam";         Password = "exam_pwd_2026"; Port = 8003 },
    @{ Folder = "certificate-service";  Package = "certificate_service";  DB = "humg_certificate";  User = "humg_certificate";  Password = "cert_pwd_2026"; Port = 8004 },
    @{ Folder = "notification-service"; Package = "notification_service"; DB = "humg_notification"; User = "humg_notification"; Password = "noti_pwd_2026"; Port = 8005 },
    @{ Folder = "cms-service";          Package = "cms_service";          DB = "humg_cms";          User = "humg_cms";          Password = "cms_pwd_2026"; Port = 8006 },
    @{ Folder = "report-service";       Package = "report_service";       DB = "humg_report";       User = "humg_report";       Password = "report_pwd_2026"; Port = 8007 }
)

$Global:PgSuperUser     = "postgres"
$Global:PgSuperPassword = "postgres"

$Global:PsqlPath = "C:\Program Files\PostgreSQL\16\bin\psql.exe"
if (-not (Test-Path $Global:PsqlPath)) {
    $Global:PsqlPath = (Get-ChildItem "C:\Program Files\PostgreSQL\*\bin\psql.exe" -ErrorAction SilentlyContinue | Select-Object -First 1).FullName
}

Write-Host "OK Config loaded. Services: $($Global:Services.Count)" -ForegroundColor Green
if ($Global:PsqlPath) {
    Write-Host "OK psql: $Global:PsqlPath" -ForegroundColor Green
} else {
    Write-Host "WARN: Khong tim thay psql.exe!" -ForegroundColor Yellow
}