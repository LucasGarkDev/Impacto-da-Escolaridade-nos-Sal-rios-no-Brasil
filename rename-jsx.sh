#!/bin/bash

echo "🔍 Procurando arquivos .js que contenham JSX..."

find ./src -type f -name "*.js" | while read file; do
  if grep -qE '<[A-Za-z]|/>' "$file"; then
    newfile="${file%.js}.jsx"
    echo "📦 Renomeando: $file → $newfile"
    mv "$file" "$newfile"
  fi
done

echo "✅ Renomeação concluída!"