import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { Check } from 'lucide-react';

export default function PricingPage() {
  const plans = [
    {
      name: 'Starter',
      price: '$29',
      description: 'Perfect for small businesses just getting started',
      features: [
        'Up to 1,000 inventory items',
        'Basic analytics',
        'Email support',
        '2 team members',
        'Mobile app access',
      ],
    },
    {
      name: 'Professional',
      price: '$79',
      description: 'Ideal for growing businesses with more demands',
      features: [
        'Up to 10,000 inventory items',
        'Advanced analytics',
        'Priority support',
        '5 team members',
        'API access',
        'Custom reports',
      ],
    },
    {
      name: 'Enterprise',
      price: 'Custom',
      description: 'For large businesses with custom requirements',
      features: [
        'Unlimited inventory items',
        'Custom analytics',
        '24/7 dedicated support',
        'Unlimited team members',
        'Custom integrations',
        'Dedicated account manager',
        'Custom deployment',
      ],
    },
  ];

  return (
    <div className="min-h-screen bg-gray-50 py-24">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <h1 className="text-4xl font-extrabold text-gray-900 sm:text-5xl sm:tracking-tight lg:text-6xl">
            Simple, transparent pricing
          </h1>
          <p className="mt-5 text-xl text-gray-500">
            Choose the perfect plan for your business
          </p>
        </div>

        <div className="mt-24 space-y-12 lg:space-y-0 lg:grid lg:grid-cols-3 lg:gap-x-8">
          {plans.map((plan) => (
            <Card key={plan.name} className="relative p-8 bg-white border border-gray-200 rounded-2xl shadow-sm flex flex-col">
              <div className="flex-1">
                <h3 className="text-xl font-semibold text-gray-900">{plan.name}</h3>
                <p className="mt-4 flex items-baseline text-gray-900">
                  <span className="text-5xl font-extrabold tracking-tight">{plan.price}</span>
                  {plan.price !== 'Custom' && <span className="ml-1 text-xl font-semibold">/month</span>}
                </p>
                <p className="mt-6 text-gray-500">{plan.description}</p>

                <ul role="list" className="mt-6 space-y-6">
                  {plan.features.map((feature) => (
                    <li key={feature} className="flex">
                      <Check className="flex-shrink-0 w-6 h-6 text-green-500" />
                      <span className="ml-3 text-gray-500">{feature}</span>
                    </li>
                  ))}
                </ul>
              </div>

              <Button className="mt-8 w-full">
                {plan.name === 'Enterprise' ? 'Contact sales' : 'Start free trial'}
              </Button>
            </Card>
          ))}
        </div>
      </div>
    </div>
  );
}