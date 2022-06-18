Set-Location "E:\OI\Luogu-Solution"
$prob = Read-Host "Problem"
git checkout -b $prob
python.exe .\files.py $prob
$null = Read-Host "Write mkdocs.yml file, press Enter key to continue"
$message = Read-Host "Message"
git add *
if ($message -eq "d")
{ git commit -m "$prob C++ AC" }
else
{ git commit -m $message }
git checkout main
Clear-Host