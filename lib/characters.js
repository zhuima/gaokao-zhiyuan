import { endpoint } from '@/utils/endpoint'

export async function getAllCharacters() {
  const data = await fetch(`${endpoint}/characters`, { cache: 'no-store' })
  if (!data.ok) {
    throw new Error('Failed to fetch')
  }
  return data.json()
}

export async function getCharacterBySlug() {}
