/** @type {import('next').NextConfig} */
// https://zenn.dev/duo3/articles/dbb8115309059e

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
