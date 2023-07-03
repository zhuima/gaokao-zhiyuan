/**
Renders a navigation component with a sticky header, containing a logo and a link to take a quiz.
@component
@returns {JSX.Element} The rendered navigation component.
*/

import Link from 'next/link'
import { Container } from '.'
import Image from 'next/image'
import { TbArrowBigRightFilled } from 'react-icons/tb'

export const Navigation = () => {
  return (
    <div className="sticky top-0 backdrop-blur-xl bg-[rgba(0,0,0,0.8)] border-b border-slate-800 z-50">
      <Container className="flex justify-between py-5">
        <Link
          href="/"
          className="flex justify-center items-center text-center w-12 h-12 logo-gif"
        >
          <Image
            id="logo"
            src="/logo.svg"
            alt="Family Guy"
            width={70}
            height={50}
            priority={true}
          />
          <Image
            className="relative bottom-1 left-1"
            id="logoBg"
            src="/fire.gif"
            alt="fire background"
            width={70}
            height={50}
            priority={true}
          ></Image>
        </Link>
        <Link
          href="/cities"
          className="flex items-center justify-center px-3 font-semibold text-black transition-colors bg-green-500 rounded-md duration-600 hover:bg-green-600"
        >
          高校导航
        </Link>
        <Link
          href="/university"
          className="flex items-center justify-center font-semibold text-white "
        >
          高校检索
        </Link>
        {/* <SignInButton />

        <AuthCheck>
          <SignOutButton />
        </AuthCheck> */}
      </Container>
    </div>
  )
}
