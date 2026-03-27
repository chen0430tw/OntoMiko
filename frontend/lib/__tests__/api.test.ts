/**
 * API module tests
 */

import { divineText } from '../api'

// Mock fetch
global.fetch = jest.fn()

describe('divineText', () => {
  beforeEach(() => {
    jest.clearAllMocks()
  })

  it('calls the correct API endpoint', async () => {
    ;(global.fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => ({
        category: '宇宙同意',
        state: 'qY',
        reason: '测试',
      }),
    })

    await divineText('测试文本')

    expect(global.fetch).toHaveBeenCalledWith(
      'http://127.0.0.1:8000/divine/text',
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: '测试文本' }),
      }
    )
  })

  it('returns the parsed JSON response', async () => {
    const mockResponse = {
      category: '宇宙同意',
      state: 'qY',
      reason: '测试通过',
      permission_score: 0.9,
    }

    ;(global.fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => mockResponse,
    })

    const result = await divineText('测试文本')

    expect(result).toEqual(mockResponse)
  })

  it('throws an error when API request fails', async () => {
    ;(global.fetch as jest.Mock).mockResolvedValueOnce({
      ok: false,
    })

    await expect(divineText('测试文本')).rejects.toThrow('API request failed')
  })

  it('throws an error when network fails', async () => {
    ;(global.fetch as jest.Mock).mockRejectedValueOnce(new Error('Network error'))

    await expect(divineText('测试文本')).rejects.toThrow('API request failed')
  })
})
