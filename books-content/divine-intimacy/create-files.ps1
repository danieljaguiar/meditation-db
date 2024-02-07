for ($i = 322; $i -le 365; $i++) {
    New-Item -Path ".\$i.md" -ItemType File -Force
  }