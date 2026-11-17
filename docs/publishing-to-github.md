# Publishing this repository to GitHub

The repository can be used offline without GitHub. To publish it:

1. On GitHub, create a **new empty repository** named `raspberry-pi-ai-lab` under your account. Leave all GitHub initialization boxes unchecked (do not add a README, license, or .gitignore since those already exist here).
2. Extract the supplied ZIP and open a terminal **inside its `raspberry-pi-ai-lab/` directory**.
3. Run:

```bash
git init -b main
git add .
git commit -m "Add offline Raspberry Pi AI workshop curriculum"
git remote add origin git@github.com:rich-bart/raspberry-pi-ai-lab.git
git push -u origin main
```

SSH push requires a GitHub SSH key already set up; alternatively use an HTTPS remote and authenticate with GitHub's supported credential manager. Once published, `README.md` becomes the front page and the lesson links work as a table of contents.

**Privacy check before pushing:** run `git status` and confirm that `data/private/` and `data/public/` are ignored. The instructor's answer key should NEVER be committed. All scripts and lesson content can safely be committed.

If the ZIP was generated with its own local Git history, GitHub publishing commands should start at `git remote add origin ...`, not `git init`.
