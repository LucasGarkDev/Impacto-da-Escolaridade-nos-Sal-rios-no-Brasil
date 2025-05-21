// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import { fileURLToPath } from 'url';

// 🧭 Emula __dirname corretamente
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      components: path.resolve(__dirname, 'src/components'),
      assets: path.resolve(__dirname, 'src/assets'),
      layouts: path.resolve(__dirname, 'src/layouts'),
      examples: path.resolve(__dirname, 'src/examples'),
      context: path.resolve(__dirname, 'src/context'),
      variables: path.resolve(__dirname, 'src/variables'),
    },
  },
});

