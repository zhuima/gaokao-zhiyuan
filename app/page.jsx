/**

Renders a Next.js page component that displays a grid of character avatars with links to individual character pages.
@component
@returns {JSX.Element} The rendered page component.
*/
import { Container } from '@/components'

export default async function Page() {
  // console.log('source item content', data)
  return (
    <main>
      <Container className="grid grid-cols-2 gap-1 py-5 md:grid-cols-3 lg:grid-cols-4">
        <h2>高等院校三千所 👨‍🎓 助力考生选大学</h2>
      </Container>
    </main>
  )
}
