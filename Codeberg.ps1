python build.py cb-pages
git switch --orphan pages
ls | grep -v build | rm -r -f
mv build/* .
git add .
git commit -m "Pages Build & Deploy"
git push codeberg pages
git branch -d pages
git checkout main
