/**
 * Retrieves a character and their associated quotes based on the provided slug.
 *
 * @param {Object} req - The request object.
 * @param {Object} params - The route parameters.
 * @param {string} params.name - The slug of the character.
 *
 * @returns {Promise<Object>} A promise that resolves to an object containing the character and their quotes, or an error response.
 */

import qoutes from '@/data/qoutes.json'
import { NextResponse } from 'next/server'

export async function GET(req, { params }) {
  try {
    console.log('id', params)
    // const university = qoutes.data.find(item => item.city_id === 12)
    const universities = qoutes.data.flatMap(city =>
      city.university.filter(u => u.name.includes(params.name)),
    )

    // console.log('character', character)
    if (!universities) {
      return new NextResponse('Not Found University', { status: 404 })
    }

    return NextResponse.json({
      universities,
    })
  } catch (error) {
    return new NextResponse('Internal Server Error', { status: 500 })
  }
}
