import git
repo = git.Repo('/var/lib/jenkins/workspace/python_git/python')
with repo.config_reader() as git_config:
    print(git_config.get_value('user', 'email'))
    print(git_config.get_value('user', 'name'))
if repo.is_dirty(untracked_files=True):
  print("Changes Detected")
  repo.git.add(all=True)
  repo.index.commit("Commit Done")
  print(repo.remotes.origin.push())
else:
  print("No Changes")
