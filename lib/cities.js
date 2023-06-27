import { endpoint } from '@/utils/endpoint'

export async function getAllCities() {
  const data = await fetch(`${endpoint}/cities`, { cache: 'no-store' })
  if (!data.ok) {
    throw new Error('Failed to fetch')
  }
  return data.json()
}

export async function getCityBySlug(slug) {
  const data = await fetch(`${endpoint}/cities/${slug}`, {
    cache: 'no-store',
  })
  if (!data.ok) {
    return new Error('Failed to fetch character slug data')
  }

  return data.json()
}
