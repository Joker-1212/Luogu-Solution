Set-Location "E:\Programming\OI\OI-Notes"
$prob = Read-Host "Problem"
git add *
$message = Read-Host "Message"
if ($message -eq "d" -or $message -eq "") {
    git commit -m "$prob C++ Finish"
}
else {
    git commit -m $message
}
git checkout main
git merge $prob
$null = Read-Host "Please reslove conflicts and submit the changes in VSCode, then press Enter key to continue"
git push github
git push gitee
git branch -d $prob
Clear-Host