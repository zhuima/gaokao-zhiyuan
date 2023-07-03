/**

Renders a Next.js page component that displays a grid of character avatars with links to individual character pages.
@component
@returns {JSX.Element} The rendered page component.
*/
import { Container } from '@/components'
import Link from 'next/link'
import { getAllCities } from '@/lib/cities'

export const metadata = {
  title: '高校省份导航',
  description:
    '全国大学三千所，助力考生选大学，各省市高校导航，高考志愿填报系统，高考志愿填报网站，中国大学目录，全国大学目录',
  keywords: [
    '各省市高校清单',
    '高考填志愿',
    '高考志愿填报',
    '高考志愿填报系统',
    '高考志愿填报网站',
    '中国大学目录',
  ],
}

export async function generateStaticParams() {
  const cities = await getAllCities()

  return cities.cities.map(city => ({ slug: city.slug }))
}

export default async function Page() {
  const cities = await getAllCities()

  return (
    <>
      <h2 className="px-5 w-full h-full max-w-screen-md m-auto mt-4 text-xl font-bold">
        高校省份导航
      </h2>

      <Container className="grid grid-cols-2 gap-1 py-5 md:grid-cols-3 lg:grid-cols-4">
        {cities?.cities?.map(item => {
          return (
            <div key={item.name} className="flex items-center">
              <div className="group relative mx-auto w-96 overflow-hidden rounded-[16px] bg-gray-300 p-[1px] transition-all duration-300 ease-in-out hover:bg-gradient-to-r hover:from-indigo-500 hover:via-purple-500 hover:to-pink-500">
                <div className="group-hover:animate-spin-slow invisible absolute -top-40 -bottom-40 left-10 right-10 bg-gradient-to-r from-transparent via-white/90 to-transparent group-hover:visible"></div>
                <div className="relative rounded-[15px] bg-white p-6">
                  <div className="space-y-4">
                    <Link
                      href={`/cities/${item.slug}`}
                      key={item.name}
                      className="flex justify-center flex-grow px-2 py-1"
                    >
                      <p className="text-lg font-semibold text-slate-800">
                        {item.name}
                      </p>
                    </Link>
                  </div>
                </div>
              </div>
            </div>
          )
        })}
      </Container>
    </>
  )
}
