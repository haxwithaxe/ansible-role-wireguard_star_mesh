wireguard_star_mesh
=========

Setup a star topology point to point wireguard mesh.

Requirements
------------

None

Role Variables
--------------

### Global Vars
- `wireguard_config_path` (optional): The directory the final wireguard config lives in. Defaults to `/etc/wireguard`.
- `wireguard_network_name` (optional): The network/interface name for this wireguard network. Defaults to `wg0`.
- `wireguard_port` (optional): The default value for the port the wireguard service listens on. Defaults to 51820.

### Host Vars
- `wireguard_ip` (required): The wireguard IP address.
- `wireguard_allowed_ips` (optional): A list of additional `AllowedIPs` values to use for this host's `Peer` entry in other hosts' configs. Defaults to an empty list.
- `wireguard_allowed_ip_cidr` (optional): The CIDR netmask suffix for the automatic `AllowedIPs` value made with `wireguard_ip`. Defaults to 32.
- `wireguard_endpoint` (optional): The `Endpoint` value to use for this host's `Peer` entry in other hosts' configs. Defaults to `ansible_hostname`.
- `wireguard_port` (optional): The port that this host's wireguard service listens on. Defaults to the global `wireguard_port`.

Dependencies
------------

None

Example Playbook
----------------

### Simple

#### host_vars

- A
    ```yaml
    wireguard_ip: 10.0.0.1
    ```

- B
    ```yaml
    wireguard_ip: 10.0.0.2
    ```

- C
    ```yaml
    wireguard_ip: 10.0.0.3
    ```


#### Playbook
```yaml
- hosts: wireguard_mesh
  roles:
     - haxwithaxe.wireguard_star_mesh
```

### Less Simple

#### host_vars

- A
    ```yaml
    wireguard_ip: 10.0.0.1
    wireguard_allowed_ips:
      - 192.168.1.0/24
    wireguard_port: 8765
    ```

- B
    ```yaml
    wireguard_ip: 10.0.0.2
    wireguard_allowed_ips:
      - 192.168.2.0/24
    wireguard_port: 23456
    wireguard_endpoint: 172.16.0.2
    ```

- C
    ```yaml
    wireguard_ip: 10.0.0.3
    wireguard_allowed_ips:
      - 192.168.3.0/24
    wireguard_endpoint: another-hostname.example.com
    ```

#### Playbook
```yaml
- hosts: wireguard_mesh
  roles:
     - role: haxwithaxe.wireguard_star_mesh
       vars:
         wireguard_network_name: hello
         wireguard_port: 12345
```

License
-------

GPLv3

Author Information
------------------

haxwithaxe spam@haxwithaxe.net
