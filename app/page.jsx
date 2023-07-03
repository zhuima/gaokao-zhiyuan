/**

Renders a Next.js page component that displays a grid of character avatars with links to individual character pages.
@component
@returns {JSX.Element} The rendered page component.
*/
import Link from 'next/link'

import { Container, BackgroundCircles } from '@/components'

export default async function Page() {
  // console.log('source item content', data)

  return (
    <div className="dark:bg-[#111a31] bg-gray-50">
      <div className="flex max-w-5xl mx-auto flex-col items-center justify-center min-h-screen flex max-w-5xl mx-auto flex-col items-center justify-center py-2 mt-10">
        <div className=" z-0">
          <BackgroundCircles />
        </div>

        <main className="flex z-10 flex-1 w-full flex-col items-center justify-center text-center px-4 -mt-60 ">
          <h1 className="mx-auto z-2 -mt-30  font-bold text-3xl tracking-tight text-slate-900 md:text-4xl sm:text-5xl dark:text-white">
            高等院校三千所 助力考生选大学{' '}
            <p className="relative whitespace-nowrap text-blue-600 mt-5">
              <svg
                aria-hidden="true"
                viewBox="0 0 418 42"
                className="absolute top-2/3 left-0 h-[0.58em] w-full fill-blue-300/70"
                preserveAspectRatio="none"
              >
                <path d="M203.371.916c-26.013-2.078-76.686 1.963-124.73 9.946L67.3 12.749C35.421 18.062 18.2 21.766 6.004 25.934 1.244 27.561.828 27.778.874 28.61c.07 1.214.828 1.121 9.595-1.176 9.072-2.377 17.15-3.92 39.246-7.496C123.565 7.986 157.869 4.492 195.942 5.046c7.461.108 19.25 1.696 19.17 2.582-.107 1.183-7.874 4.31-25.75 10.366-21.992 7.45-35.43 12.534-36.701 13.884-2.173 2.308-.202 4.407 4.generateS442 4.734 2.654.187 3.263.157 15.593-.78 35.401-2.686 57.944-3.488 88.365-3.143 46.327.526 75.721 2.23 130.788 7.584 19.787 1.924 20.814 1.98 24.557 1.332l.066-.011c1.201-.203 1.53-1.825.399-2.335-2.911-1.31-4.893-1.604-22.048-3.261-57.509-5.556-87.871-7.36-132.059-7.842-23.239-.254-33.617-.116-50.627.674-11.629.54-42.371 2.494-46.696 2.967-2.359.259 8.133-3.625 26.504-9.81 23.239-7.825 27.934-10.149 28.304-14.005.417-4.348-3.529-6-16.878-7.066Z" />
              </svg>
              <span className="relative mt-10">成功上岸</span>
            </p>
          </h1>

          <p className="mx-auto mt-6 max-w-2xl text-lg tracking-tight text-slate-700 dark:text-gray-200">
            本站数据来自
            <Link
              href="https://laosheng.top/fuwu/yuanxiao"
              className=" text-blue-600 transition-colors hover:bg-blue-100  mt-6"
              target="_blank"
              rel="noopener noreferrer"
            >
              「老生常谈」
            </Link>
            的网站，本站做了数据处理。
          </p>
          {/* <p className="text-slate-700 mt-5 dark:text-gray-300">
              5196 site summaries generated so far.
            </p> */}
          {/* <Toaster
            position="top-center"
            reverseOrder={false}
            toastOptions={{ duration: 2000 }}
          />
          <hr className="h-px bg-gray-700 border-1 dark:bg-gray-700" />
          <ResizablePanel>
            <AnimatePresence mode="wait">
              <motion.div className="space-y-10 my-10">
                {generatedSummary && (
                  <>
                    <div>
                      <h2 className="sm:text-4xl dark:text-white text-3xl font-bold text-slate-900 mx-auto">
                        Your generated summary
                      </h2>
                    </div>
                    <div className="space-y-8 dark:text-white flex flex-col items-center justify-center max-w-xl mx-auto">
                      <div
                        className="rounded-xl dark:text-white p-4 dark:bg-gray-200 bg-gray-100 transition cursor-copy border text-md shadow-inner font-semibold text-left"
                        onClick={() => {
                          navigator.clipboard.writeText(
                            generatedSummary.toString(),
                          )
                          toast('Summary copied to clipboard', {
                            icon: '✂️',
                          })
                        }}
                      >
                        <p className={'dark:text-black'}>{generatedSummary}</p>

                        <a
                          href={`https://twitter.com/intent/tweet?text=${encodeURIComponent(
                            `I honestly had no idea what ${url} did until I used siteexplainer.com 🔥`,
                          )}`}
                          target="_blank"
                          className="text-[#1da1f2] font-medium text-sm px-5 py-2.5 text-center inline-flex items-center hover:opacity-80"
                        >
                          <svg
                            className="w-4 h-4 mr-2 -ml-1"
                            aria-hidden="true"
                            focusable="false"
                            data-prefix="fab"
                            data-icon="twitter"
                            role="img"
                            xmlns="http://www.w3.org/2000/svg"
                            viewBox="0 0 512 512"
                          >
                            <path
                              fill="currentColor"
                              d="M459.4 151.7c.325 4.548 .325 9.097 .325 13.65 0 138.7-105.6 298.6-298.6 298.6-59.45 0-114.7-17.22-161.1-47.11 8.447 .974 16.57 1.299 25.34 1.299 49.06 0 94.21-16.57 130.3-44.83-46.13-.975-84.79-31.19-98.11-72.77 6.498 .974 12.99 1.624 19.82 1.624 9.421 0 18.84-1.3 27.61-3.573-48.08-9.747-84.14-51.98-84.14-102.1v-1.299c13.97 7.797 30.21 12.67 47.43 13.32-28.26-18.84-46.78-51.01-46.78-87.39 0-19.49 5.197-37.36 14.29-52.95 51.65 63.67 129.3 105.3 216.4 109.8-1.624-7.797-2.599-15.92-2.599-24.04 0-57.83 46.78-104.9 104.9-104.9 30.21 0 57.5 12.67 76.67 33.14 23.72-4.548 46.46-13.32 66.6-25.34-7.798 24.37-24.37 44.83-46.13 57.83 21.12-2.273 41.58-8.122 60.43-16.24-14.29 20.79-32.16 39.31-52.63 54.25z"
                            ></path>
                          </svg>
                          Share on Twitter
                        </a>
                      </div>
                    </div>
                  </>
                )}
              </motion.div>
            </AnimatePresence>
          </ResizablePanel> */}
        </main>
      </div>
    </div>
  )
}
