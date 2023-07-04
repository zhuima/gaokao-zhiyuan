/**
 * Root layout component for the Family Guy app.
 *
 * @component
 * @param {Object} props - The component props.
 * @param {ReactNode} props.children - The child components.
 * @returns {JSX.Element} The rendered root layout.
 */

import NextTopLoader from 'nextjs-toploader'

import { Inter } from 'next/font/google'
import { Navigation } from '@/components'
import ScrollToTop from '@/components/ScrollToTopButton'
import './globals.css'

// import Authprovider from './Authprovider'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: '高考志愿指南',
  description: '高考志愿指南，高考志愿填报指南，中国大学三千所，助力考生选大学',
  keywords: [
    '高考填志愿',
    '高考志愿填报',
    '高考志愿填报系统',
    '高考志愿填报网站',
    '中国大学目录',
  ],
}

export default function RootLayout({ children }) {
  return (
    <html lang="en" suppressHydrationWarning={true}>
      <body className={inter.className} suppressHydrationWarning={true}>
        <NextTopLoader />
        <Navigation />
        {children}
        <ScrollToTop />
      </body>
    </html>
  )
}
