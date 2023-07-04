import Link from 'next/link'
import { Container } from '@/components'

export default function UniversityQueryList({ source, name }) {
  return (
    <>
      {source.length > 0 ? (
        <Container className="flex flex-col gap-5 py-5">
          <h2 className="mt-10 text-xl font-bold">高校清单</h2>
          <span>
            包含 <span className="text-blue-500">{name} </span> 关键字的高校有{' '}
            <span className="text-blue-500">{source.length} </span> 所
          </span>
          <ul className="grid gap-2 sm:grid-cols-2">
            {source?.map((item, idx) => {
              return (
                <div
                  key={idx}
                  className="flex flex-col border rounded-lg overflow-hidden bg-white"
                >
                  <div className="grid grid-cols-1 sm:grid-cols-4">
                    <div className="flex flex-col border-b sm:border-b-0 items-center p-8 sm:px-4 sm:h-full sm:justify-center">
                      <p className="text-4xl font-bold text-[#0ed3cf] rounded-full">
                        HN
                      </p>
                    </div>
                    <div className="flex flex-col sm:border-l col-span-3">
                      <div className="flex flex-col space-y-4  p-6 text-gray-600">
                        <div className="flex flex-row text-sm">
                          <span className="mr-3">
                            <svg
                              xmlns="http://www.w3.org/2000/svg"
                              enableBackground="new 0 0 24 24"
                              height="20px"
                              viewBox="0 0 24 24"
                              width="20px"
                              fill="#64748b"
                            >
                              <g>
                                <rect fill="none" height="24" width="24" />
                              </g>
                              <g>
                                <path d="M20,7h-5V4c0-1.1-0.9-2-2-2h-2C9.9,2,9,2.9,9,4v3H4C2.9,7,2,7.9,2,9v11c0,1.1,0.9,2,2,2h16c1.1,0,2-0.9,2-2V9 C22,7.9,21.1,7,20,7z M9,12c0.83,0,1.5,0.67,1.5,1.5S9.83,15,9,15s-1.5-0.67-1.5-1.5S8.17,12,9,12z M12,18H6v-0.75c0-1,2-1.5,3-1.5 s3,0.5,3,1.5V18z M13,9h-2V4h2V9z M18,16.5h-4V15h4V16.5z M18,13.5h-4V12h4V13.5z" />
                              </g>
                            </svg>
                          </span>
                          <p className="flex items-center  text-gray-500">
                            <span className="font-semibold mr-2 text-xs uppercase">
                              名称:
                            </span>
                            <span>{item.name}</span>
                          </p>
                        </div>

                        <div className="flex flex-row text-sm">
                          <span className="mr-3">
                            <svg
                              xmlns="http://www.w3.org/2000/svg"
                              height="20px"
                              viewBox="0 0 24 24"
                              width="20px"
                              fill="#64748b"
                            >
                              <path d="M0 0h24v24H0z" fill="none" />
                              <path d="M17 12h-5v5h5v-5zM16 1v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2h-1V1h-2zm3 18H5V8h14v11z" />
                            </svg>
                          </span>
                          <p className="flex items-center  text-gray-500">
                            <span className="font-semibold mr-2 text-xs uppercase">
                              地址:
                            </span>
                            <span>{item.addr}</span>
                          </p>
                        </div>
                      </div>
                      {item.link && (
                        <div className="flex flex-col w-full relative bottom-0">
                          <div className="grid grid-cols-3 border-t divide-x text-[#0ed3cf]  bg-gray-50 dark:bg-transparent py-3">
                            <Link
                              href={item.link}
                              target="_blank"
                              className="cursor-pointer uppercase text-xs flex flex-row items-center justify-center font-semibold"
                            >
                              <div className="mr-2">
                                <svg
                                  xmlns="http://www.w3.org/2000/svg"
                                  height="20px"
                                  viewBox="0 0 24 24"
                                  width="20px"
                                  fill="#0ed3cf"
                                >
                                  <path d="M0 0h24v24H0z" fill="none" />
                                  <path d="M19 19H5V5h7V3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z" />
                                </svg>
                              </div>
                              官网
                            </Link>
                          </div>
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              )
            })}
          </ul>
        </Container>
      ) : (
        <Container className="flex flex-col gap-5 py-5">
          <h2 className="mt-10 text-xl font-bold">高校清单</h2>
          <span>
            包含 <span className="text-blue-500">{name} </span> 关键字的高校
            <span className="text-blue-500">不存在</span>
          </span>
        </Container>
      )}
    </>
  )
}
