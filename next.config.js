/** @type {import('next').NextConfig} */
// https://zenn.dev/duo3/articles/dbb8115309059e
const dns = require('dns')
dns.setDefaultResultOrder('ipv4first')

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

module.exports = nextConfig
