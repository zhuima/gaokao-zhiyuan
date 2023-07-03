'use client'
import { useState, Suspense } from 'react'
import { getUniversityByFilter } from '@/lib/universities'
import UniversityQueryList from '@/components/UniversityQueryList'

export default function SearchForm() {
  const [searchResults, setSearchResults] = useState([])
  const [keyword, setKeyword] = useState('')
  // 获取搜索框的内容, 前面犯了一个错误，拿就是组件也搞成了异步，导致浏览器资源一直飙升，而页面加载老是失败, 2023-07-02 问题倒腾了好久
  const filterUniversity = async event => {
    event.preventDefault()
    const name = event.target.name.value

    const res = await getUniversityByFilter(name)
    setKeyword(name)
    setSearchResults(res.universities)
    console.log('name', name, '------->,resuls', searchResults)
  }

  return (
    <>
      <div className="mt-10 flex justify-center items-center">
        <div className="container mx-auto bg-indigo-500 rounded-lg p-14">
          <form onSubmit={filterUniversity} className="group">
            <h1 className="text-center font-bold text-white text-2xl tracking-tight text-slate-900 sm:text-5xl">
              快来搜一搜你心仪的大学
            </h1>

            <div className="flex mt-10 sm:flex items-center bg-white rounded-lg overflow-hidden px-2 py-3 justify-between">
              <label htmlFor="name"></label>
              <input
                className="text-base text-gray-400 flex-grow outline-none px-2 focus:border-gray-500 focus:outline-none valid:[&:not(:placeholder-shown)]:border-green-500 [&:not(:placeholder-shown):not(:focus):invalid~span]:block invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-400"
                id="name"
                name="name"
                type="text"
                placeholder="根据大学名称或关键字检索"
                autocomplete="off"
                required
              />
              {/* <input
                type="text"
                name="name"
                id="name"
                placeholder="根据大学名称或关键字检索"
                class="w-full rounded-md border border-gray-300 px-3 py-2.5 placeholder-gray-300 shadow shadow-gray-100 focus:border-gray-500 focus:outline-none valid:[&:not(:placeholder-shown)]:border-green-500 [&:not(:placeholder-shown):not(:focus):invalid~span]:block invalid:[&:not(:placeholder-shown):not(:focus)]:border-red-400"
                autocomplete="off"
                required
              /> */}
              <span className="mt-2 hidden text-sm text-red-400">
                请输入有效的关键字或高校名称.{' '}
              </span>
              <button className="bg-indigo-500 text-white text-base rounded-lg px-4 py-2 font-thin focus:bg-indigo-600 focus:outline-none group-invalid:pointer-events-none group-invalid:opacity-70">
                搜索
              </button>
            </div>
          </form>
        </div>
      </div>
      {searchResults.length > 1 && (
        <Suspense fallback={<p>加载中...</p>}>
          <UniversityQueryList source={searchResults} name={keyword} />
        </Suspense>
      )}
    </>
  )
}
