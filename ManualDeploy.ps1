python build.py cb-pages
$pagesbranchexists = (git branch --list pages) -Eq $null
if ($pagesbranchexists) {
    git branch -D pages
}
git switch --orphan pages
ls | grep -v build | rm -r -fo
mv build/* .
git add .
git commit -m "Pages Build & Deploy"
git push codeberg pages -f
git push roundabout pages -f
