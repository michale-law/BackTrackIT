import { Navbar } from '@/components/navbar'
import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import { BarChart2, Package, Users, Truck } from 'lucide-react'

export default function Home() {
  return (
    <main className="min-h-screen bg-white">
      <Navbar />
      
      {/* Hero Section */}
      <section className="relative bg-gradient-to-b from-green-50 to-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
          <div className="text-center">
            <h1 className="text-4xl tracking-tight font-extrabold text-gray-900 sm:text-5xl md:text-6xl">
              <span className="block">Smart Inventory Management</span>
              <span className="block text-green-600">for Modern Businesses</span>
            </h1>
            <p className="mt-3 max-w-md mx-auto text-base text-gray-500 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl">
              Streamline your inventory tracking, boost efficiency, and make data-driven decisions with BackTrackIt's comprehensive management solution.
            </p>
            <div className="mt-5 max-w-md mx-auto sm:flex sm:justify-center md:mt-8">
              <div className="rounded-md shadow">
                <Button size="lg" className="w-full sm:w-auto">
                  Start Free Trial
                </Button>
              </div>
              <div className="mt-3 sm:mt-0 sm:ml-3">
                <Button size="lg" variant="outline" className="w-full sm:w-auto">
                  Watch Demo
                </Button>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h2 className="text-3xl font-extrabold text-gray-900">
              Everything you need to manage your inventory
            </h2>
            <p className="mt-4 text-lg text-gray-500">
              Powerful features to help you track, analyze, and optimize your stock levels.
            </p>
          </div>

          <div className="mt-20">
            <div className="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4">
              <Card className="p-6">
                <Package className="h-12 w-12 text-green-600" />
                <h3 className="mt-4 text-lg font-medium text-gray-900">Real-time Tracking</h3>
                <p className="mt-2 text-base text-gray-500">
                  Monitor your inventory levels in real-time across all locations.
                </p>
              </Card>

              <Card className="p-6">
                <BarChart2 className="h-12 w-12 text-green-600" />
                <h3 className="mt-4 text-lg font-medium text-gray-900">Analytics & Reports</h3>
                <p className="mt-2 text-base text-gray-500">
                  Get insights with detailed analytics and customizable reports.
                </p>
              </Card>

              <Card className="p-6">
                <Users className="h-12 w-12 text-green-600" />
                <h3 className="mt-4 text-lg font-medium text-gray-900">Team Collaboration</h3>
                <p className="mt-2 text-base text-gray-500">
                  Work together seamlessly with role-based access control.
                </p>
              </Card>

              <Card className="p-6">
                <Truck className="h-12 w-12 text-green-600" />
                <h3 className="mt-4 text-lg font-medium text-gray-900">Supply Chain Integration</h3>
                <p className="mt-2 text-base text-gray-500">
                  Connect with suppliers and logistics partners effortlessly.
                </p>
              </Card>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-green-700">
        <div className="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:py-16 lg:px-8 lg:flex lg:items-center lg:justify-between">
          <h2 className="text-3xl font-extrabold tracking-tight text-white sm:text-4xl">
            <span className="block">Ready to get started?</span>
            <span className="block text-green-200">Start your free trial today.</span>
          </h2>
          <div className="mt-8 flex lg:mt-0 lg:flex-shrink-0">
            <div className="inline-flex rounded-md shadow">
              <Button size="lg" variant="secondary">
                Get Started
              </Button>
            </div>
          </div>
        </div>
      </section>
    </main>
  )
}