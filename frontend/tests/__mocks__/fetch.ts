/**
 * Fetch mock for testing
 */

export const mockFetch = jest.fn()

global.fetch = mockFetch
