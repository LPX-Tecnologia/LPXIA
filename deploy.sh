#!/bin/bash
cd /home/luiz-felipe-paixao/Documentos/lpxIA/LPX-NEXUS
rm -rf .git
git init
git branch -M main
git remote add origin https://github.com/LPX-Tecnologia/LPXIA.git
git add .
git commit -m "Site LPXIA - LPX-NEXUS"
git push -u origin main --force
echo "PRONTO - Verifique https://github.com/LPX-Tecnologia/LPXIA"
