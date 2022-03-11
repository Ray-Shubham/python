import git
repo = git.Repo('python')
if repo.is_dirty(untracked_files=True):
  print("Changes Detected")
  repo.git.add(all=True)
  repo.index.commit("Commit Done")
  print(repo.remotes.origin.push())
else:
  print("No Changes")
