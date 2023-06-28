'use client' // Error components must be Client Components

import { Container } from '@/components'
import { useEffect } from 'react'
import Link from 'next/link'

export default function Error(error, reset) {
  useEffect(() => {
    // Log the error to an error reporting service
    console.error(error)
  }, [error])

  return (
    <Container className="flex flex-col items-center gap-5 py-5">
      {/* <h1 className="text-2xl">Something Went Wrong!</h1>
      <button
        className="px-5 py-2 bg-blue-700 rounded-md"
        onClick={() => reset()}
      >
        Try again
      </button> */}

      <section className="bg-white dark:bg-gray-900 my-16">
        <div className="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">
          <div className="mx-auto max-w-screen-sm text-center">
            <h1 className="mb-4 text-7xl tracking-tight lg:text-9xl text-primary-600 dark:text-primary-500">
              404
            </h1>
            <p className="mb-4 text-3xl tracking-tight font-bold text-gray-900 md:text-4xl dark:text-white">
              {' '}
              呜呼
            </p>
            <p className="mb-4 text-lg font-light text-gray-500 dark:text-gray-400">
              你访问的页面被外星人抓走了.
            </p>
            <Link
              href="/cities"
              className="inline-flex text-white bg-black dark:bg-white dark:text-black p-3 hover:bg-gray-800 my-4"
            >
              返回高校列表
            </Link>
          </div>
        </div>
      </section>
    </Container>
  )
}
