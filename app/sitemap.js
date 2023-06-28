// app/sitemap.js
// https://claritydev.net/blog/nextjs-dynamic-sitemap-pages-app-directory

const URL = 'https://gkzy.ruankao.eu.org'

export default async function sitemap() {
  const routes = ['', '/cities'].map(route => ({
    url: `${URL}${route}`,
    lastModified: new Date().toISOString(),
  }))

  return [...routes]
}
