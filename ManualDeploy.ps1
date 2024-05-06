python build.py cb-pages
git switch --orphan pages
ls | grep -v build | rm -r -fo
mv build/* .
git add .
git commit -m "Pages Build & Deploy"
git push codeberg pages -f
git push roundabout www -f
git branch -d pages
git checkout main
