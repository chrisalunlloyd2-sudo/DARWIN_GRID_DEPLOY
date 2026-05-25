import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        main()

if __name__ == '__main__':
    unittest.main()
```

[CMD]
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/chrisalunlloyd2-sudo/DARWIN_GRID_DEPLOY.git
git push -u origin main
