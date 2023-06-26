/** @type {import('next').NextConfig} */
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
