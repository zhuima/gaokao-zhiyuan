/**
 * Retrieves a list of characters from the characters.json file.
 * @returns {Promise<Object>} A promise that resolves to an object containing the characters data.
 */

import qoutes from '@/data/qoutes.json'

import { NextResponse } from 'next/server'

export async function GET(req, { params }) {
  const name = req.nextUrl.searchParams.get('name')
  try {
    console.log('id', params, '------', name)
    // const university = qoutes.data.find(item => item.city_id === 12)
    const universities = qoutes.data.flatMap(city =>
      city.university.filter(u => u.name.includes(name)),
    )

    // console.log('character', character)
    if (!universities) {
      return new NextResponse('Not Found University', { status: 404 })
    }

    return NextResponse.json({
      universities: name ? universities : qoutes.data,
    })
  } catch (error) {
    return new NextResponse('Internal Server Error', { status: 500 })
  }
}
