/** @type {import('next').NextConfig} */
import dns from 'dns'

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
