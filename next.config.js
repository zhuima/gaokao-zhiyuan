/** @type {import('next').NextConfig} */
// https://zenn.dev/duo3/articles/dbb8115309059e
import { setDefaultResultOrder } from 'dns'
setDefaultResultOrder('ipv4first')

const nextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'res.cloudinary.com',
      },
    ],
  },
}

export default nextConfig
