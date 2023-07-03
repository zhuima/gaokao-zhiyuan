// import { NEXT_PUBLIC_API } from '@/utils/NEXT_PUBLIC_API'

export async function getUniversityByFilter(name) {
  console.log(
    'name',
    name,
    '------->',
    `${process.env.NEXT_PUBLIC_API}/university?name=${name}`,
  )
  const data = await fetch(
    `${process.env.NEXT_PUBLIC_API}/university?name=${name}`,
  )
  // const data = await fetch(`http://127.0.0.1:3000/api/university?name=${name}`)
  if (!data.ok) {
    throw new Error('Failed to fetch')
  }
  return data.json()
}

export async function getUniversityByName(name) {
  const data = await fetch(
    `${process.env.NEXT_PUBLIC_API}/university/${name}`,
    {
      cache: 'no-store',
    },
  )
  if (!data.ok) {
    return new Error('Failed to fetch character slug data')
  }

  return data.json()
}
