import yaml


def test_yaml2():
    env = {
        "default": "dev",
        "list": {
            "dev": "127.0.0.1",
            "test": "127.0.0.2"
        }
    }
    with open("env.yaml", "w") as f:
        yaml.safe_dump(data=env, stream=f)

if __name__ == '__main__':
    test_yaml2()
