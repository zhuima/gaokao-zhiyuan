// import { NEXT_PUBLIC_API } from '@/utils/NEXT_PUBLIC_API'

export async function getAllCities() {
  const data = await fetch(`${process.env.NEXT_PUBLIC_API}/cities`)
  if (!data.ok) {
    throw new Error('Failed to fetch')
  }
  return data.json()
}

export async function getCityBySlug(slug) {
  const data = await fetch(`${process.env.NEXT_PUBLIC_API}/cities/${slug}`)
  if (!data.ok) {
    return new Error('Failed to fetch character slug data')
  }

  return data.json()
}
