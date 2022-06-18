Set-Location "E:\OI\Luogu-Solution"
$prob = Read-Host "Problem"
git checkout -b $prob | Out-Null
python.exe .\files.py $prob
$null = Read-Host "Write mkdocs.yml file, press Enter key to continue"
$message = Read-Host "Message"
git add * | Out-Null
if ($message -eq "d")
{ git commit -m "$prob C++ AC" | Out-Null }
else
{ git commit -m $message | Out-Null }
git checkout main | Out-Null
