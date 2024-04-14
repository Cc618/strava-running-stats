import api
import pandas as pd


def make_stats(df):
    stats = df.copy()

    # min/km
    stats['pace'] = (stats['time'] / 60) / (stats['distance'] / 1000)
    stats = stats.groupby('kind').agg({'distance': ['mean'], 'time': ['mean'], 'pace': ['mean', 'count']})

    return stats


def show_stats(activities):
    # Make buckets
    buckets = [5, 10, 15, 20, 30, 40]
    ratio = .1
    max_thres = 3
    bucket_activities = []
    for b in buckets:
        lowerbound = max(b * (1 - ratio), b - max_thres)
        upperbound = min(b * (1 + ratio), b + max_thres)
        bucket_activities.append({'lowerbound': lowerbound, 'upperbound': upperbound, 'kind': b, 'activities': []})

    # Add activities
    for activity in activities:
        # Find bucket
        dist = activity['distance'] / 1000
        bucket = next((bucket for bucket in bucket_activities if bucket['lowerbound'] <= dist <= bucket['upperbound']), None)
        if bucket is not None:
            bucket['activities'].append(activity)

    # Create dataframe
    df = {'kind': [], 'distance': [], 'time': []}
    for bucket in bucket_activities:
        for activity in bucket['activities']:
            df['kind'].append(bucket['kind'])
            df['distance'].append(activity['distance'])
            df['time'].append(activity['moving_time'])

    df = pd.DataFrame(df)

    # Make / show stats
    print(len(df), 'activities')
    print('Raw data:')
    stats = make_stats(df)
    print(stats)

    print()
    print('Summary:')
    for kind, row in stats.iterrows():
        cnt = int(row['pace']['count'])
        pace = row['pace']['mean']
        pacem = int(pace)
        paces = int((pace - pacem) * 60)
        print(f"- {kind:>2d}K: {pacem}:{paces:02d}min/km ({60/pace:.1f}km/h) ({cnt} activities)")


def example():
    activities = [
        {'distance': 5000, 'moving_time': 60 * 5 * 5},
        {'distance': 5100, 'moving_time': 60 * 5.2 * 5},
        {'distance': 10500, 'moving_time': 60 * 6 * 10}
    ]
    show_stats(activities)


if __name__ == '__main__':
    max_pages = 20

    all_activities = []
    print('Fetching activities')
    for page in range(1, max_pages + 1):
        print('Page', page)
        try:
            activities = api.fetch('/athlete/activities', params={'page': page})
            if not activities:
                break
            all_activities += activities
        except:
            break

    assert all_activities, 'Cannot access api'

    print()
    show_stats(all_activities)
