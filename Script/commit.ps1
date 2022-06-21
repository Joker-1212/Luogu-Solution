Set-Location "E:\Programming\OI\OI-Notes"
$prob = Read-Host "Problem"
git checkout -b $prob
python.exe .\Script\files.py $prob
$message = Read-Host "Write mkdocs.yml file, enter message here and press Enter key to continue"
git add *
if ($message -eq "d" -or $message -eq "")
{ git commit -m "$prob C++ AC" }
elseif ($message -eq "exit") {
    git checkout main
    git branch -D $prob
}
else
{ git commit -m $message }
git checkout main
Clear-Host