import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from "@tailwindcss/vite";

// https://vite.dev/config/
export default defineConfig({
  plugins: [
      react(),
      tailwindcss()
      ],
  server: {
       proxy: {
           '/api': {
               target: 'http://127.0.0.1:8000',
               changeOrigin: true,
           }
       }
  },
  optimizeDeps: {
        include: [
            'antd',
            '@ant-design/icons',
            '@ant-design/icons/es/components/AntdIcon',
        ],
        force: true,
    },
    resolve: {
        alias: {
            '@ant-design/icons/es': '@ant-design/icons/lib',
        },
    },
})
