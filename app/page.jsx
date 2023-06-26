/**

Renders a Next.js page component that displays a grid of character avatars with links to individual character pages.
@component
@returns {JSX.Element} The rendered page component.
*/

import { Container } from '@/components'
import Image from 'next/image'
import Link from 'next/link'
import { getAllCharacters } from '@/lib/characters'

export default async function Page() {
  const data = await getAllCharacters()

  console.log('source item content', data)
  return (
    <main>
      <Container className="grid grid-cols-2 gap-1 py-5 md:grid-cols-3 lg:grid-cols-4">
        {data?.characters?.map(item => {
          return (
            <div key={item.name} className="flex items-center">
              <div className="group relative mx-auto w-96 overflow-hidden rounded-[16px] bg-gray-300 p-[1px] transition-all duration-300 ease-in-out hover:bg-gradient-to-r hover:from-indigo-500 hover:via-purple-500 hover:to-pink-500">
                <div className="group-hover:animate-spin-slow invisible absolute -top-40 -bottom-40 left-10 right-10 bg-gradient-to-r from-transparent via-white/90 to-transparent group-hover:visible"></div>
                <div className="relative rounded-[15px] bg-white p-6">
                  <div className="space-y-4">
                    <Link
                      href={`/characters/${item.slug}`}
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
    </main>
  )
}
