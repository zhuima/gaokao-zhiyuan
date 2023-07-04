'use client'
import { useEffect, useState } from 'react'

function ReadingBar() {
  const [completion, setCompletion] = useState(0)

  useEffect(() => {
    const updateScrollCompletion = () => {
      const currentProgress = window.scrollY
      const scrollHeight = document.body.scrollHeight - window.innerHeight
      if (scrollHeight) {
        setCompletion(Number((currentProgress / scrollHeight).toFixed(2)) * 100)
      }
    }

    window.addEventListener('scroll', updateScrollCompletion)

    return () => {
      window.removeEventListener('scroll', updateScrollCompletion)
    }
  }, [])

  return (
    <span
      style={{ transform: `translateX(${completion - 100}%)` }}
      className="absolute bg-yellow-400 h-1 w-full bottom-0"
    />
  )
}
export default ReadingBar
