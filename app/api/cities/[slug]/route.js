/**
 * Retrieves a character and their associated quotes based on the provided slug.
 *
 * @param {Object} req - The request object.
 * @param {Object} params - The route parameters.
 * @param {string} params.slug - The slug of the character.
 *
 * @returns {Promise<Object>} A promise that resolves to an object containing the character and their quotes, or an error response.
 */

import cities from '@/data/cities.json'
import qoutes from '@/data/qoutes.json'
import { NextResponse } from 'next/server'

export async function GET(req, { params }) {
  try {
    // console.log('id', params.slug)
    const city = cities.data.find(item => item.slug === params.slug)
    // console.log('character', character)
    if (!city) {
      return new NextResponse('Not Found City', { status: 404 })
    }

    const city_qoutes = qoutes.data.filter(item => item.city_id === city.id)

    return NextResponse.json({
      city,
      city_qoutes: city_qoutes.length > 0 ? city_qoutes : null,
    })
  } catch (error) {
    return new NextResponse('Internal Server Error', { status: 500 })
  }
}
