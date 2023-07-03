/**

Renders a Next.js page component that displays a grid of character avatars with links to individual character pages.
@component
@returns {JSX.Element} The rendered page component.
*/
import SearchForm from '@/components/SearchForm'

export const metadata = {
  title: '高校检索',
  description:
    '全国大学三千所，助力考生选大学，各省市高校导航，高考志愿填报系统，高考志愿填报网站，中国大学目录，全国大学目录',
  keywords: [
    '高校按名称检索',
    '高校按专业检索',
    '高校按关键字检索',
    '高考志愿填报网站',
    '中国大学目录',
    '全国高校三千所',
  ],
}

export default async function Page() {
  return <SearchForm />
}
