// 'use client'

// import { useSession, signIn, signOut } from 'next-auth/react'
// import Image from 'next/image'
// import Link from 'next/link'

// export function SignInButton() {
//   const { data: session, status } = useSession()
//   console.log(session, status)

//   if (status === 'authenticated') {
//     return (
//       <Link href={`/cities`}>
//         <Image
//           src={session.user?.image ?? '/mememan.webp'}
//           width={32}
//           height={32}
//           alt="Your Name"
//         />
//       </Link>
//     )
//   }

//   return (
//     <button
//       onClick={() => signIn()}
//       className="text-white font-semibold text-black transition-colors  rounded-md duration-600 hover:bg-green-600"
//     >
//       Sign in
//     </button>
//   )
// }

// export function SignOutButton() {
//   return (
//     <button
//       onClick={() => signOut()}
//       className="text-white  font-semibold text-black transition-colors  rounded-md duration-600 hover:bg-green-600"
//     >
//       Sign out
//     </button>
//   )
// }
