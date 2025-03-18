/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  eslint: {
    ignoreDuringBuilds: true,
  },
  images: { unoptimized: true },
  // Add trailing slashes for better Safari compatibility
  trailingSlash: true,
};

module.exports = nextConfig;