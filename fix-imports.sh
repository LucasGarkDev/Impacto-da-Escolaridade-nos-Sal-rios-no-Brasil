#!/bin/bash

echo "🔧 Corrigindo imports de .js para .jsx..."

# Encontra todos os arquivos .jsx
find ./src -type f -name "*.jsx" | while read jsx_file; do
  # Extrai o nome base do arquivo, sem extensão
  base_name=$(basename "$jsx_file" .jsx)

  # Procura e atualiza todos os arquivos que fazem importações para esse nome sem extensão ou com .js
  find ./src -type f \( -name "*.js" -o -name "*.jsx" \) | while read file; do
    sed -i "s|\(['\"]\)\(.*${base_name}\)\.js\1|\1\2.jsx\1|g" "$file"
    sed -i "s|\(['\"]\)\(.*${base_name}\)\1|\1\2.jsx\1|g" "$file"
  done
done

echo "✅ Imports atualizados com sucesso!"
